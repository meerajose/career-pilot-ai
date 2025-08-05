from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="CareerPilot AI API",
    description="AI-powered career assistant API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ResumeAnalysisRequest(BaseModel):
    resume_text: str

class ResumeAnalysisResponse(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    score: int

class JobMatchRequest(BaseModel):
    resume_text: str
    job_description: str

class JobMatchResponse(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    recommendations: List[str]
    overall_assessment: str

class CoverLetterRequest(BaseModel):
    resume_text: str
    job_description: str
    company_name: str
    job_title: str
    your_name: str
    your_email: str
    your_phone: Optional[str] = ""

class CoverLetterResponse(BaseModel):
    cover_letter: str

class InterviewFeedbackRequest(BaseModel):
    question: str
    answer: str
    category: str

class InterviewFeedbackResponse(BaseModel):
    feedback: str
    score: int
    suggestions: List[str]

# Mock AI analysis functions (replace with actual AI implementation)
def analyze_resume(resume_text: str) -> ResumeAnalysisResponse:
    """Mock resume analysis - replace with actual AI implementation"""
    # This would typically use OpenAI API or other AI service
    return ResumeAnalysisResponse(
        strengths=[
            "Strong technical skills in React and TypeScript",
            "Good project management experience",
            "Clear communication skills demonstrated"
        ],
        weaknesses=[
            "Limited leadership experience",
            "Could add more quantifiable achievements",
            "Missing certifications section"
        ],
        suggestions=[
            "Add specific metrics and achievements (e.g., 'Increased performance by 25%')",
            "Include relevant certifications",
            "Add a summary section at the top",
            "Use more action verbs in descriptions"
        ],
        score=78
    )

def match_job(resume_text: str, job_description: str) -> JobMatchResponse:
    """Mock job matching - replace with actual AI implementation"""
    return JobMatchResponse(
        match_score=82,
        matched_skills=[
            "React.js",
            "TypeScript",
            "JavaScript",
            "Git",
            "REST APIs",
            "HTML/CSS"
        ],
        missing_skills=[
            "Python",
            "Docker",
            "AWS",
            "Machine Learning"
        ],
        recommendations=[
            "Consider learning Python for backend development",
            "Get familiar with Docker for containerization",
            "Learn AWS services for cloud deployment",
            "Take an introductory course in Machine Learning"
        ],
        overall_assessment="You have a strong foundation in frontend development and would be a good fit for this role. Focus on learning the missing backend and cloud skills to increase your match score."
    )

def generate_cover_letter(data: CoverLetterRequest) -> CoverLetterResponse:
    """Mock cover letter generation - replace with actual AI implementation"""
    cover_letter = f"""Dear Hiring Manager,

I am writing to express my strong interest in the {data.job_title} position at {data.company_name}. With my background in software development and passion for creating innovative solutions, I am excited about the opportunity to contribute to your team.

My experience includes developing scalable web applications using modern technologies such as React, TypeScript, and Node.js. I have successfully delivered projects that improved user experience and system performance, demonstrating my ability to work effectively in fast-paced environments.

I am particularly drawn to {data.company_name} because of your commitment to innovation and excellence. Your focus on creating impactful solutions aligns perfectly with my professional goals and technical expertise.

I would welcome the opportunity to discuss how my skills and experience can contribute to your team's success. Thank you for considering my application.

Best regards,
{data.your_name}
{data.your_email}
{data.your_phone}"""

    return CoverLetterResponse(cover_letter=cover_letter)

def analyze_interview_answer(question: str, answer: str, category: str) -> InterviewFeedbackResponse:
    """Mock interview feedback - replace with actual AI implementation"""
    return InterviewFeedbackResponse(
        feedback="Good answer! You covered the main points well. Consider adding more specific examples and metrics to make your response stronger. Your communication was clear and structured.",
        score=85,
        suggestions=[
            "Add specific examples from your experience",
            "Include quantifiable results when possible",
            "Structure your response using the STAR method",
            "Practice speaking more confidently"
        ]
    )

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Welcome to CareerPilot AI API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "CareerPilot AI API"}

@app.post("/analyze-resume", response_model=ResumeAnalysisResponse)
async def analyze_resume_endpoint(request: ResumeAnalysisRequest):
    """Analyze resume and provide AI-powered suggestions"""
    try:
        if not request.resume_text.strip():
            raise HTTPException(status_code=400, detail="Resume text cannot be empty")
        
        result = analyze_resume(request.resume_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/match-job", response_model=JobMatchResponse)
async def match_job_endpoint(request: JobMatchRequest):
    """Match resume with job description and identify skill gaps"""
    try:
        if not request.resume_text.strip() or not request.job_description.strip():
            raise HTTPException(status_code=400, detail="Both resume text and job description are required")
        
        result = match_job(request.resume_text, request.job_description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Job matching failed: {str(e)}")

@app.post("/generate-cover-letter", response_model=CoverLetterResponse)
async def generate_cover_letter_endpoint(request: CoverLetterRequest):
    """Generate a personalized cover letter"""
    try:
        required_fields = ['resume_text', 'job_description', 'company_name', 'job_title', 'your_name', 'your_email']
        for field in required_fields:
            if not getattr(request, field).strip():
                raise HTTPException(status_code=400, detail=f"{field.replace('_', ' ').title()} is required")
        
        result = generate_cover_letter(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cover letter generation failed: {str(e)}")

@app.post("/analyze-answer", response_model=InterviewFeedbackResponse)
async def analyze_interview_answer_endpoint(request: InterviewFeedbackRequest):
    """Analyze interview answer and provide feedback"""
    try:
        if not request.question.strip() or not request.answer.strip():
            raise HTTPException(status_code=400, detail="Both question and answer are required")
        
        result = analyze_interview_answer(request.question, request.answer, request.category)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Answer analysis failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 