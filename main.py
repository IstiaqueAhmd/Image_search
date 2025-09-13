from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from image_service import search_image
from schema import ImageQuery
# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/images", response_model=list)
async def image_finder(Request: ImageQuery):
    try:
        imageList = search_image(Request.image_query)
        return imageList
    except:
        raise HTTPException(status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
