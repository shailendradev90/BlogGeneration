# BlogAgentic 📝

An AI-powered blog generation system built with LangChain, LangGraph, and FastAPI. This project uses agentic workflows to automatically generate SEO-friendly blog content with optional multi-language translation support.

## 🌟 Features

- **Automated Blog Generation**: Generate complete blog posts with titles and content based on any topic
- **Multi-language Support**: Translate blog content to Hindi and French
- **LangGraph Workflows**: Utilizes state-based graph workflows for structured content generation
- **FastAPI Backend**: RESTful API for easy integration
- **Groq LLM Integration**: Powered by Groq's fast LLM inference (llama-3.1-8b-instant)
- **LangSmith Integration**: Built-in observability and monitoring

## 🏗️ Architecture

The project uses a graph-based architecture with LangGraph:

### Topic-Only Workflow
```
START → Title Creation → Content Generation → END
```

### Language Translation Workflow
```
START → Title Creation → Content Generation → Route → [Hindi/French Translation] → END
```

## 📋 Prerequisites

- Python >= 3.13
- Groq API Key
- LangChain API Key (for LangSmith)

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BlogAgentic
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

## 💻 Usage

### Running the FastAPI Server

Start the development server:
```bash
python app.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Generate Blog (Topic Only)
```bash
POST /blogs
Content-Type: application/json

{
  "topic": "Artificial Intelligence in Healthcare"
}
```

#### Generate Blog with Translation
```bash
POST /blogs
Content-Type: application/json

{
  "topic": "Artificial Intelligence in Healthcare",
  "language": "hindi"
}
```

Supported languages: `hindi`, `french`

### Response Format
```json
{
  "data": {
    "topic": "Artificial Intelligence in Healthcare",
    "blog": {
      "title": "Generated Blog Title",
      "content": "Generated blog content..."
    },
    "current_language": "hindi"
  }
}
```

## 📁 Project Structure

```
BlogAgentic/
├── src/
│   ├── graphs/
│   │   └── graph_builder.py    # LangGraph workflow definitions
│   ├── nodes/
│   │   └── blog_node.py        # Node implementations (title, content, translation)
│   ├── states/
│   │   └── blogstate.py        # State definitions for workflows
│   └── llms/
│       └── groqllm.py          # Groq LLM configuration
├── app.py                       # FastAPI application
├── main.py                      # Entry point
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project configuration
└── langgraph.json              # LangGraph configuration
```

## 🔧 Components

### GraphBuilder
Manages the creation and compilation of LangGraph workflows:
- `build_topic_graph()`: Simple blog generation workflow
- `build_language_graph()`: Blog generation with translation support

### BlogNode
Contains the core logic for blog generation:
- `title_creation()`: Generates SEO-friendly blog titles
- `content_generation()`: Creates detailed blog content
- `translation()`: Translates content to specified language
- `route_decision()`: Routes to appropriate translation node

### BlogState
TypedDict defining the state structure:
- `topic`: The blog topic
- `blog`: Blog object with title and content
- `current_language`: Target language for translation

## 🛠️ Development

### LangGraph Studio
The project includes configuration for LangGraph Studio visualization:
```bash
langgraph dev
```

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key
- `LANGCHAIN_API_KEY`: Your LangChain API key (for LangSmith)
- `LANGSMITH_API_KEY`: Automatically set from LANGCHAIN_API_KEY

## 📦 Dependencies

- **langchain**: LLM framework
- **langgraph**: Graph-based workflow orchestration
- **langchain-groq**: Groq LLM integration
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🔮 Future Enhancements

- [ ] Add more language support
- [ ] Implement blog post editing and refinement
- [ ] Add image generation for blog posts
- [ ] Support for different blog styles and tones
- [ ] Database integration for storing generated blogs
- [ ] User authentication and management

## 📞 Support

For issues and questions, please open an issue in the repository.

---

Built with ❤️ using LangChain, LangGraph, and FastAPI