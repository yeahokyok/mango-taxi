import "./App.css"
import { Route, Routes } from "react-router-dom"

import Home from "./components/Home"
import LogIn from "./components/LogIn"
import SignUp from "./components/SignUp"

function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="signup" element={<SignUp />} />
            <Route path="login" element={<LogIn />} />
        </Routes>
    )
}

export default App
