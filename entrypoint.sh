#!/bin/sh

/bin/ollama serve &
pid=$!

echo "🚀 Ollama is running..."

echo "📥 Downloading deepseek-r1:1.5b model..."

ollama pull deepseek-r1:1.5b

echo "✅ deepseek-r1:1.5b model downloaded successfully!"

ollama run deepseek-r1:1.5b

echo "🚀 deepseek-r1:1.5b model running!"

wait $pid