'use client'
import { useEffect, useState } from 'react';
function App() {

  const [descState, setDescState] = useState([])

  const ds_change = (index, data) => {
    const newItem = {index, data}
    if (!descState[index]) {
      setDescState(setDescState([...descState, data]))
    }
    
    console.log(descState[index])
  }

  return (
    <div>
      <p>Yes</p>
      <p onClick={() => ds_change(0,0)}>Yes</p>
    </div>
  );
}
export default App;
