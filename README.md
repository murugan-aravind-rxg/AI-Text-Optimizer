# 🎯 AI-Powered Text Optimization System

This system implements an intelligent feedback loop that continuously refines text using Large Language Models (LLMs) until it meets quality standards.

## 🔧 How It Works

1. **Text Input**: You provide initial text that needs improvement
2. **Optimization Loop**: The system iteratively refines the text through:
   - **LLM Optimizer**: Generates improved versions with creativity (temperature=0.7)
   - **LLM Evaluator**: Assesses quality with consistency (temperature=0.0)
   - **Feedback Integration**: Uses evaluation feedback for next iteration
3. **Quality Control**: Continues until text meets quality threshold or max iterations
4. **Final Output**: Returns the best optimized version

## 🎨 Key Features

- **Multi-Provider Support**: Works with Groq and OpenAI LLMs
- **Intelligent Evaluation**: Uses AI to judge text quality objectively
- **Iterative Improvement**: Each iteration builds on previous feedback
- **Quality Threshold**: Configurable acceptance criteria (default: 0.7 score)
- **Flexible Configuration**: Adjustable iterations and providers

## 🚀 Use Cases

- Content refinement and enhancement
- Technical documentation improvement
- Marketing copy optimization
- Academic writing enhancement
- Code documentation clarity
- Any text that needs professional polish

## 💡 Technical Highlights

- Temperature control for different tasks (creative vs. consistent)
- Robust error handling and validation
- Clear, maintainable code structure
- Comprehensive documentation
- Self-documenting variable names

## 📋 Requirements

```bash
pip install openai anthropic python-dotenv
```

## 🔑 Environment Variables

Create a `.env` file with your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Quick Start

```python
from passageRefiner import optimize_prompt

# Your text to optimize
text = "Your text here that needs improvement"

# Optimize the text
optimized_text = optimize_prompt(text, provider="groq", max_iterations=5)

print(f"🎯 Final Output: {optimized_text}")
```

## 🔄 Workflow Example

```python
# Example workflow
prompt = "The selected candidate will be responsible for customizing LLM for specific use cases..."

# The system will:
# 1. Generate improved versions
# 2. Evaluate each version
# 3. Use feedback for next iteration
# 4. Return the best version

final_output = optimize_prompt(prompt, provider="groq")
```

## 🎛️ Configuration Options

| Parameter | Default | Description |
|-----------|---------|-------------|
| `provider` | `"groq"` | LLM provider ("groq" or "openai") |
| `max_iterations` | `5` | Maximum optimization attempts |
| `temperature` (optimizer) | `0.7` | Creativity level for text generation |
| `temperature` (evaluator) | `0.0` | Consistency level for evaluation |

## 📊 Performance Metrics

The system tracks:
- Number of iterations performed
- Quality scores for each version
- Acceptance/rejection decisions
- Final output quality

## 🔍 How Evaluation Works

The evaluator uses a scoring system (0-1):
- **Score ≥ 0.7**: Text is accepted as high quality
- **Score < 0.7**: Text needs improvement, feedback provided
- **Temperature = 0**: Ensures consistent evaluation results

## 🛠️ Customization

You can customize:
- Quality threshold (default: 0.7)
- Maximum iterations
- LLM providers and models
- Evaluation criteria
- Output formatting

## 📝 Example Output

```
🔄 Iteration 1
🧠 Optimized: [Improved version of your text]
❌ Feedback: [Detailed feedback on what needs improvement]

🔄 Iteration 2
🧠 Optimized: [Further improved version]
✅ Accepted by evaluator

🎯 Final Output: [Your optimized text]
```

## 🤝 Contributing

Feel free to contribute by:
- Improving the evaluation criteria
- Adding new LLM providers
- Enhancing error handling
- Optimizing performance

## 📄 License

This project is open source and available under the MIT License.

---

**This system transforms the way we approach text improvement by leveraging AI to provide objective, iterative refinement that consistently produces high-quality results.**
