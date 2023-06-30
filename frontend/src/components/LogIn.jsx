import React from "react"
import { Link } from "react-router-dom"
import { Breadcrumb, Card, Col, Row } from "react-bootstrap"

function LogIn(props) {
    return (
        <Row>
            <Col lg={12}>
                <Breadcrumb>
                    <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                    <Breadcrumb.Item active>Log in</Breadcrumb.Item>
                </Breadcrumb>
                <Card>
                    <Card.Header>Log in</Card.Header>
                    <Card.Body></Card.Body>
                    <p className="mt-3 text-center">
                        Don't have an account?{" "}
                        <Link to="/signup">Sign up!</Link>
                    </p>
                </Card>
            </Col>
        </Row>
    )
}

export default LogIn
