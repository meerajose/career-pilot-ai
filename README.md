# CareerPilot AI

An AI-powered career assistant that helps job seekers improve their resumes, match with jobs, generate cover letters, and practice interviews.

## Features

- **Resume Analyzer**: Get AI-powered suggestions to improve your resume
- **Job Matcher**: Compare your resume with job descriptions and identify skill gaps
- **Cover Letter Generator**: Create personalized cover letters based on your resume and job requirements
- **Interview Coach**: Practice mock interviews with AI feedback

## Tech Stack

### Frontend
- React 19 with TypeScript
- Tailwind CSS for styling
- React Router for navigation

### Backend
- FastAPI (Python)
- Pydantic for data validation
- CORS middleware for cross-origin requests

## Project Structure

```
careerpilot-ai/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── ResumeAnalyzer.tsx
│   │   │   ├── JobMatcher.tsx
│   │   │   ├── CoverLetterGenerator.tsx
│   │   │   └── InterviewCoach.tsx
│   │   ├── App.tsx          # Main app component with routing
│   │   └── index.css        # Tailwind CSS styles
│   ├── package.json
│   └── tailwind.config.js
├── backend/                  # FastAPI backend application
│   ├── main.py              # Main FastAPI application
│   └── requirements.txt     # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   python main.py
   ```

The backend API will be available at `http://localhost:8000`

### API Documentation

Once the backend is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## API Endpoints

### Resume Analysis
- `POST /analyze-resume` - Analyze resume and provide suggestions

### Job Matching
- `POST /match-job` - Match resume with job description

### Cover Letter Generation
- `POST /generate-cover-letter` - Generate personalized cover letter

### Interview Coaching
- `POST /analyze-answer` - Analyze interview answers and provide feedback

## Development

### Frontend Development

The frontend uses:
- **React Router** for navigation between different features
- **Tailwind CSS** for responsive, utility-first styling
- **TypeScript** for type safety
- **Custom components** for each feature with proper state management

### Backend Development

The backend uses:
- **FastAPI** for high-performance API development
- **Pydantic** for data validation and serialization
- **CORS middleware** to allow frontend communication
- **Mock AI functions** that can be replaced with actual AI services

### Adding Real AI Integration

To integrate with real AI services (like OpenAI):

1. Add your API keys to a `.env` file in the backend directory
2. Replace the mock functions in `main.py` with actual AI API calls
3. Update the frontend API calls to use the real endpoints

Example `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Future Enhancements

- User authentication and profile management
- Save and manage multiple resumes
- Advanced AI models for better analysis
- Integration with job boards
- Video interview practice
- Resume template library
- Export functionality for generated documents 
