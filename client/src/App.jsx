import { useState } from 'react'

import './App.css'
import PostCreate from './components/PostCreate'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <PostCreate/>
    </>
  )
}

export default App
