import React, { useState } from "react"
import { Link, Navigate } from "react-router-dom"
import { Breadcrumb, Button, Card, Col, Form, Row } from "react-bootstrap"
import { Formik } from "formik"

function LogIn(props) {
    const [isSubmitted, setSubmitted] = useState(false)
    const onSubmit = (values, actions) => setSubmitted(true)
    if (isSubmitted) {
        return <Navigate to="/" />
    }
    return (
        <Row>
            <Col lg={12}>
                <Breadcrumb>
                    <Breadcrumb.Item href="/">Home</Breadcrumb.Item>
                    <Breadcrumb.Item active>Log in</Breadcrumb.Item>
                </Breadcrumb>
                <Card>
                    <Card.Header>Log in</Card.Header>
                    <Card.Body>
                        <Formik
                            initialValues={{
                                username: "",
                                password: "",
                            }}
                            onSubmit={onSubmit}
                        >
                            {({ handleChange, handleSubmit, values }) => (
                                <Form noValidate onSubmit={handleSubmit}>
                                    <Form.Group controlId="username">
                                        <Form.Label>Username:</Form.Label>
                                        <Form.Control
                                            name="username"
                                            onChange={handleChange}
                                            value={values.username}
                                        />
                                    </Form.Group>
                                    <Form.Group controlId="password">
                                        <Form.Label>Password:</Form.Label>
                                        <Form.Control
                                            name="password"
                                            onChange={handleChange}
                                            type="password"
                                            value={values.password}
                                        />
                                    </Form.Group>
                                    <Button
                                        block
                                        type="submit"
                                        variant="primary"
                                    >
                                        Log in
                                    </Button>
                                </Form>
                            )}
                        </Formik>
                        <Card.Text className="text-center">
                            Don't have an account?{" "}
                            <Link to="/signup">Sign up!</Link>
                        </Card.Text>
                    </Card.Body>
                </Card>
            </Col>
        </Row>
    )
}

export default LogIn
