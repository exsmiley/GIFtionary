var builder = require('botbuilder');

var connector = new builder.ConsoleConnector().listen();
var bot = new builder.UniversalBot(connector, [
    function (session) {
        session.send("What is your name?");
    },
    function(session, results) {
        session.send("You are: ", results);
    }
]);