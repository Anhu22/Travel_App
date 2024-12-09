const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

console.log('JavaScript file is connected!');
// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/Travel_App', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

// Create a schema and model
const userSchema = new mongoose.Schema({
    username: String,
    firstName: String,
    middleName: String,
    lastName: String,
    password: String
});

const User = mongoose.model('User ', userSchema);

// Serve static files (like your HTML)
app.use(express.static('public'));

// Handle form submission
app.post('/signup', (req, res) => {
    const newUser  = new User({
        username: req.body.username,
        firstName: req.body.fname,
        middleName: req.body.mname,
        lastName: req.body.lname,
        password: req.body.npwd // Make sure to hash passwords in a real application
    });

    newUser .save()
        .then(() => res.send('User  registered successfully!'))
        .catch(err => res.status(400).send('Error: ' + err));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});