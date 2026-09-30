'use client'
import { useEffect, useState } from 'react';


export default function Home() {

	const [videos, setVideos] = useState([]);
	const [displayVideos, setDisplayVideos] = useState([]);
	const [searchTerm, setSearchTerm] = useState('');
	const [loading, setLoading] = useState(true);
	const [randomVideos, setRandomVideos] = useState([])

	let colors = {
		"bu_lgray" : "bg-pink-200 text-black p-2 rounded-lg mr-2",
		"vi_pink" : "bg-pink-200 p-5 rounded-2xl m-5",
		"border" : "border-pink-400 border-3",
		"hover" : "hover:bg-pink-500"
	}

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
			// behavior: 'smooth',
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
		return videos[randomIndex];
	}
	const all = () => {
		setDisplayVideos(videos)
	}

	const descShow = (index) => {
		const nextFilteredVideos = filteredVideos.map((video, i) => {
			if (i=== index) {
				if (video.descState == "hidden") {
					video.descState = ""
					video.showHide = "Hide Description"
				} else if (video.descState == "") {
					video.descState = "hidden"
					video.showHide = "Show description"
				}
				return video
			} else { return video}
		})
		setDisplayVideos(nextFilteredVideos)
	}


	return (
		<div>
			{loading ? <p>Loading...</p> : <>
				<div className='m-5 mb-0 mt-0 pt-5'>
					<input id="text-input" type="text" placeholder='Search' value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} className='focus:ring-2 ring-0 ring-blue-200 focus:shadow-lg/20 focus:outline-none focus:border-black p-1 border border-solid border-gray-400 rounded-lg' />
				</div>
				<div className='m-5 mb-0'>
					<button onClick={random} className={`${colors.bu_lgray} ${colors.border} ${colors.hover}`}>Random Video</button>
					<button onClick={all} className={`${colors.bu_lgray} ${colors.border} ${colors.hover}`}>All Videos</button>
					<button onClick={scrollToBottom} className={`${colors.bu_lgray} ${colors.border} ${colors.hover} font-[OpenSans]`}>Scroll to the Bottom</button>
				</div>

				{filteredVideos.map((video, index) => (
					<div key={index} className={`${colors.vi_pink} ${colors.border}`}>
						<div className='flex flex-row'>
							<a className='flex-column basis-50' href={`https://www.youtube.com/watch?v=${video.video_id}&list=${video.playlist_id}`}>
								<img className='w-30' src={video.thumbnail} />
							</a>
							<div className='flex-column basis-full'>
								<a href={`https://www.youtube.com/watch?v=${video.video_id}&list=${video.playlist_id}`}>{video.title}</a>
								{video.title == "Deleted video" || video.title == "Private video" ? null : video.description ? <p
								onClick={() => {descShow(index)}}
								className='hover:underline'
								>
									{video.showHide}
								</p> : <p>No description</p>}
								
								

								<p className={video.descState}>{video.description}</p>
							</div>
						</div>

					</div>
				))}
				<div className='m-5 mb-5'>
					<button onClick={scrollToTop} className={`${colors.bu_lgray}`}>Scroll to the Top</button>
				</div>

			</>}
		</div>
	)
}
