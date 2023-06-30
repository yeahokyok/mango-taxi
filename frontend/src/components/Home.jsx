import React from "react"
import { Link } from "react-router-dom"

function Home(props) {
    return (
        <div className="middle-center">
            <h1 className="landing logo">Taxi</h1>
            <Link className="btn btn-primary" to="/signup">
                Sign up
            </Link>
            <Link className="btn btn-primary" to="/login">
                Log in
            </Link>
        </div>
    )
}

export default Home
