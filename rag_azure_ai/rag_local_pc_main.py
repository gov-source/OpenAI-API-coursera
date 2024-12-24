import uvicorn
from rag_local_pc import app

if __name__ == '__main__':
    uvicorn.run("rag_local_pc:app", host="0.0.0.0", port=8000, reload=True)