'use server'

export async function GET() {
  try {
    const response = await fetch("http://localhost:8000/video");
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response;
    console.log(result);
    return result;
  } catch (error) {
    console.error(error.message);
  }
    

}