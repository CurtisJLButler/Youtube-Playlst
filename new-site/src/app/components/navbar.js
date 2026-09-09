import Image from "next/image";
import Youtube from "./YouTube_logo_2013.svg"

export default function NavBar() {
return (
  <div className="sticky top-0 left-0 z-50 w-full p-5 pt-0">
    <div className="bg-pink-200 rounded-b-4xl p-5">
      <div className="flex flex-row mb-0 bg-pink-300 border-3 border-pink-400 rounded-2xl">
        <a href="/" className="p-4 rounded-s-xl hover:bg-pink-500">Home</a>
        <div className="bg-pink-400 mt-3 mb-3 pl-0.5"></div>
        <a href="/playlist" className="p-4 hover:bg-pink-500">Playlist</a>
        <div className="w-full bg-pink-300 rounded-e-xl"></div>
        <div className="bg-pink-400 mt-3 mb-3 pl-0.5"></div>
        <a href="https://youtube.com" className="flex items-center h-15 w-60 md:w-50 lg:w-40 p-2">
          <Image alt="Youtube.com" src={Youtube} className=" object-cover" />
        </a>
        
      </div>
    </div>
  </div>
  
)
}