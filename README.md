### `README.md`

# MkDocs Quiz Plugin

The MkDocs Quiz Plugin is a simple and effective way to turn your Markdown documentation into interactive quizzes. With this plugin, you can create multiple-choice questions directly within your Markdown files, and users can interact with these quizzes right on your site.

## Features

- **Interactive Multiple-Choice Questions**: Easily add multiple-choice questions to your Markdown files.
- **Scoring**: Users can submit their answers and receive a score.
- **Customization**: Optional feedback and other customizations via the `mkdocs.yml` file.

## Installation

To install the MkDocs Quiz Plugin, you can use pip:

```bash
pip install mkdocs-quiz-plugin
```

Or include it in your `requirements.txt` file:

```plaintext
mkdocs-quiz-plugin>=0.1.0
```

## Configuration

Add the plugin to your `mkdocs.yml` configuration file:

```yaml
plugins:
  - quiz:
      enable_feedback: true
```

### Configuration Options

- `enable_feedback` (boolean): Enables or disables immediate feedback when submitting answers. Default is `true`.

## Usage

To create a quiz, simply add a section in your Markdown file using the following format:

```markdown
## Question 1
What is the capital of France?
- [ ] Berlin
- [ ] Madrid
- [x] Paris
- [ ] Rome
```

### Example

```markdown
# Sample Quiz

## Question 1
What is the capital of France?
- [ ] Berlin
- [ ] Madrid
- [x] Paris
- [ ] Rome

## Question 2
Which planet is known as the Red Planet?
- [ ] Earth
- [x] Mars
- [ ] Jupiter
- [ ] Saturn
```

This will render as an interactive quiz where users can select their answers and submit them to see their scores.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy quizzing with MkDocs!
```

