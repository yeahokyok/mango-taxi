import "./App.css"
import { Route, Routes } from "react-router-dom"
import { Container, Navbar } from "react-bootstrap"
import { LinkContainer } from "react-router-bootstrap"

import Home from "./components/Home"
import LogIn from "./components/LogIn"
import SignUp from "./components/SignUp"

function App() {
    return (
        <>
            <Navbar bg="light" expand="lg" variant="light">
                <LinkContainer to="/">
                    <Navbar.Brand className="logo">Mango Taxi</Navbar.Brand>
                </LinkContainer>
                <Navbar.Toggle />
                <Navbar.Collapse></Navbar.Collapse>
            </Navbar>
            <Container className="pt-3">
                <Routes>
                    <Route path="/" element={<Home />}></Route>
                    <Route path="signup" element={<SignUp />} />
                    <Route path="login" element={<LogIn />} />
                </Routes>
            </Container>
        </>
    )
}

export default App
