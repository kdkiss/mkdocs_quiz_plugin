from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import re
import uuid

class QuizPlugin(BasePlugin):
    config_scheme = (
        ('enable_feedback', config_options.Type(bool, default=True)),
    )

    def on_page_markdown(self, markdown, page, config, files):
        return self.convert_quizzes(markdown)

    def convert_quizzes(self, markdown_text):
        # Split the markdown into quiz and non-quiz sections
        sections = re.split(r'(:::quiz.*?:::)', markdown_text, flags=re.DOTALL)
        
        result = []
        for section in sections:
            if section.strip().startswith(':::quiz'):
                # This is a quiz section
                quiz_content = section.strip()[7:-3].strip()  # Remove :::quiz and ::: delimiters
                questions = re.split(r'(##\s.*?)(?=##|\Z)', quiz_content, flags=re.DOTALL)
                quiz_html = ['<div class="quiz-container">']
                for question in questions:
                    if question.strip().startswith('##'):
                        question_match = re.match(r'##\s+(.*?)\n((?:- \(\( ?x?\)\) .+\n?)+)', question, re.DOTALL)
                        if question_match:
                            question_text = question_match.group(1).strip()
                            options_block = question_match.group(2).strip().split('\n')
                            options_html = self.generate_options_html(options_block)
                            quiz_html.append(f'<div class="quiz-question"><h2>{question_text}</h2>{options_html}</div>')
                quiz_html.append('</div>')
                result.append(''.join(quiz_html))
            else:
                # This is non-quiz content
                result.append(section)
        
        return ''.join(result)

    def generate_options_html(self, options):
        quiz_id = str(uuid.uuid4())  # Generate a unique ID for each quiz
        options_html = f'<ul class="quiz-options" data-quiz-id="{quiz_id}">'
        for option in options:
            option = option.strip()
            if option:
                correct = 'true' if '((x))' in option else 'false'
                option_text = re.sub(r'- \(\( ?x?\)\)', '', option).strip()
                options_html += f'<li data-correct="{correct}"><label><input type="radio" name="quiz-{quiz_id}"> {option_text}</label></li>'
        options_html += '</ul>'
        return options_html

    def on_post_page(self, output, page, config):
        if '<div class="quiz-container">' in output:
            output += self.generate_quiz_script()
            output += self.generate_quiz_style()
        return output

    def generate_quiz_script(self):
        return '''
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                var quizContainers = document.querySelectorAll('.quiz-container');
                quizContainers.forEach(function(quizContainer) {
                    var quizzes = quizContainer.querySelectorAll('.quiz-question');
                    var submitButton = document.createElement('button');
                    submitButton.textContent = 'Submit Quiz';
                    submitButton.className = 'quiz-submit-btn';
                    quizContainer.appendChild(submitButton);

                    submitButton.onclick = function() {
                        var score = 0;
                        var totalQuestions = quizzes.length;
                        
                        quizzes.forEach(function(quiz) {
                            var options = quiz.querySelectorAll('.quiz-options li');
                            var questionAnswered = false;
                            
                            options.forEach(function(option) {
                                var radio = option.querySelector('input[type="radio"]');
                                if (radio.checked) {
                                    questionAnswered = true;
                                    if (option.getAttribute('data-correct') === 'true') {
                                        score += 1;
                                        option.style.color = 'green';
                                    } else {
                                        option.style.color = 'red';
                                    }
                                }
                            });
                            
                            if (!questionAnswered) {
                                totalQuestions -= 1; // Don't count unanswered questions
                            }
                        });

                        var scoreDisplay = quizContainer.querySelector('.score-display');
                        if (!scoreDisplay) {
                            scoreDisplay = document.createElement('p');
                            scoreDisplay.className = 'score-display';
                            quizContainer.appendChild(scoreDisplay);
                        }
                        scoreDisplay.textContent = 'Your score: ' + score + '/' + totalQuestions;
                    };
                });
            });
        </script>
        '''

    def generate_quiz_style(self):
        return '''
        <style>
            .quiz-container {
                border: 1px solid #ddd;
                padding: 15px;
                margin-bottom: 20px;
            }
            .quiz-question {
                margin-bottom: 20px;
            }
            .quiz-options {
                list-style-type: none;
                padding-left: 0;
            }
            .quiz-options li {
                margin-bottom: 10px;
            }
            .score-display {
                font-weight: bold;
                margin-top: 10px;
            }
            .quiz-submit-btn {
                display: block;
                margin: 20px 0;
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .quiz-submit-btn:hover {
                background-color: #0056b3;
            }
        </style>
        '''