import React from "react"
import { Link } from "react-router-dom"
import { Breadcrumb, Card, Col, Row } from "react-bootstrap"

function SignUp(props) {
    return (
        <Row>
            <Col lg={12}>
                <Breadcrumb>
                    <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                    <Breadcrumb.Item active>Sign up</Breadcrumb.Item>
                </Breadcrumb>
                <Card>
                    <Card.Header>Sign up</Card.Header>
                    <Card.Body></Card.Body>
                    <p className="mt-3 text-center">
                        Already have an account?{" "}
                        <Link to="/login">Log in!</Link>
                    </p>
                </Card>
            </Col>
        </Row>
    )
}

export default SignUp