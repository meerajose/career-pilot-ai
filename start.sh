#!/bin/bash

echo "🚀 Starting CareerPilot AI..."

# Function to check if a port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null ; then
        echo "Port $1 is already in use"
        return 1
    else
        return 0
    fi
}

# Start backend
echo "📡 Starting FastAPI backend..."
cd backend
if check_port 8000; then
    source venv/bin/activate
    python main.py &
    BACKEND_PID=$!
    echo "Backend started with PID: $BACKEND_PID"
else
    echo "Backend port 8000 is already in use"
fi
cd ..

# Start frontend
echo "🎨 Starting React frontend..."
cd frontend
if check_port 3000; then
    npm start &
    FRONTEND_PID=$!
    echo "Frontend started with PID: $FRONTEND_PID"
else
    echo "Frontend port 3000 is already in use"
fi
cd ..

echo ""
echo "✅ CareerPilot AI is starting up!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for user to stop
wait 