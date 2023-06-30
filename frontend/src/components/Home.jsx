import React from "react"
import { Link } from "react-router-dom"

function Home(props) {
    return (
        <div>
            <h1>Taxi</h1>
            <Link to="/signup">Sign up</Link>
            <Link to="/login">Log in</Link>
        </div>
    )
}

export default Home
