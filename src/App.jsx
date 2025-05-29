import './App.css';
import React, {useState} from "react";
import {Button, Card, Container} from "react-bootstrap";

function App() {

    const [input, setInput] = useState('');
    const [summary, setSummary] = useState('');
    const [loading, setLoading] = useState(false);

    async function handleSummarize(e) {
        e.preventDefault();
        setLoading(true);
        setSummary('');
        try {
            const response = await fetch('http://localhost:5000/summarize', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: input}),
            });
            const data = await response.json();
            setSummary(data.summary || data.error);
            console.log(summary)
        } catch (err) {
            setSummary("Error: Could not connect to backend.");
        }
        setLoading(false);
    }

    return (
        <Container className="my-4 mx-4">
            <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
                <h1> Text Summarization </h1>
                <p>Enter text here to summarize</p>
                <textarea
                    type="text"
                    value={input}
                    onChange={e => setInput(e.target.value)}
                    placeholder="Input text"
                />
                <Button
                    onClick={handleSummarize}
                >
                    {loading ? "Summarizing ..." : "Summarize Text"}
                </Button>
                <p>The text summary is given below</p>
                <Card>
                    <Card.Body>
                        {summary ? summary : "Summary here"}
                    </Card.Body>
                </Card>
            </div>
        </Container>
    )
}

export default App;
