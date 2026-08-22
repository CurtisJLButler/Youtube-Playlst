'use client'
import { useEffect, useState } from 'react';
import Link from 'next/link'

export default function Home() {

  const [videos, setVideos] = useState([]);
  const [displayVideos, setDisplayVideos] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [randomVideos, setRandomVideos] = useState([])

   const filteredVideos = displayVideos.filter(video =>
     video.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  useEffect(() => {
    async function fetchVideos() {
      const response = await fetch('http://localhost:3000/playlist/fetch');
      const data = await response.json();
      setVideos(data.videos);
      setDisplayVideos(data.videos);
      setLoading(false);
    }
    fetchVideos();
  }, []);

  const scrollToBottom = () => {
    window.scrollTo({
      top: document.documentElement.scrollHeight, // Get the total height of the document
      // behavior: 'smooth', // Smooth animation
    })}
    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        // behavior: 'smooth',
      })}

      const random = () => {
        let randomIndex = Math.floor(Math.random() * videos.length);
        while (videos[randomIndex].title == "Deleted video" || videos[randomIndex].title == "Private video") {
          randomIndex = Math.floor(Math.random() * videos.length);
        }

        if (randomVideos.length == 0) {
          // console.log(videos[randomIndex])
          setRandomVideos([videos[randomIndex]])
          setDisplayVideos([videos[randomIndex]])
        } else if (randomVideos.length > 0) {
          let newRand = [videos[randomIndex]]
          for (let video of randomVideos) {
            newRand.push(video)
          }
          setRandomVideos(newRand)
          setDisplayVideos(newRand)
        }
        // setRandomVideos(newRand)

        return videos[randomIndex];
      }
      const all = () => {
        setDisplayVideos(videos)
      }


      return (
        <>
        {loading ? <p>Loading...</p> : <>
          <div className='m-5 mb-0'>
          <input id="text-input" type="text" placeholder='Search' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} className='p-1 border border-solid rounded' />
          <button onClick={scrollToBottom} className='bg-blue-500 hover:bg-blue-700 text-white p-1 rounded'>Scroll to Bottom of Page</button>
          </div>
          <div className='m-5 mb-0'>
          <button onClick={random} className='bg-green-500 hover:bg-green-700 text-white p-1 rounded'>Random Video</button>
          <button onClick={all} className='bg-green-500 hover:bg-green-700 text-white p-1 rounded'>All Videos</button>
          </div>
          {filteredVideos.map((video, index) => (
            <div key={index}>
            <p>{video[0]}</p>
            </div>
          ))}
          {filteredVideos.map((video, index) => (
            <div key={index} className='m-5'>
            <a href={`https://www.youtube.com/watch?v=${video.video_id}&list=${video.playlist_id}`}>
            <div className='flex flex-row'>
            <img className='w-30' src={video.thumbnail} />
            <h2>{video.title}</h2>
            </div>
            </a>

            </div>
          ))}
          <div className='m-5 mb-0'>
          <button onClick={scrollToTop} className='bg-blue-500 hover:bg-blue-700 text-white p-1 rounded'>Scroll to Top of Page</button>
          <input id="text-input" type="text" placeholder='Search' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} className='p-1 border border-solid rounded' />
          </div>

          </>}

          </>
      )
}
