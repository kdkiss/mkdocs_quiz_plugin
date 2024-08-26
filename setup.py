from setuptools import setup, find_packages

setup(
    name='mkdocs-quiz-plugin',
    version='0.1.0',
    description='A MkDocs plugin to turn markdown pages into interactive quizzes',
    long_description='This MkDocs plugin allows you to create interactive quizzes directly within your markdown pages.',
    keywords='mkdocs plugin quiz markdown',
    url='https://github.com/yourusername/mkdocs-quiz-plugin',
    author='Your Name',
    author_email='youremail@example.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'quiz = mkdocs_quiz_plugin.quiz:QuizPlugin'
        ]
    }
)
