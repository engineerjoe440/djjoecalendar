import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";

import "./App.css";
import "react-big-calendar/lib/css/react-big-calendar.css";

const localizer = momentLocalizer(moment);

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      error: null,
      events: []
    };

    // Make Default Request
    //this.requestAvailableDates({});

    // Bind Class Method
    this.requestAvailableDates = this.requestAvailableDates.bind(this);
  }

  requestAvailableDates(props) {
    // Make POST Request with JSON Payload
    fetch("/api/getavailability", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        start_year: JSON.stringify(props.start.getFullYear()),
        start_month: JSON.stringify(props.start.getMonth()),
        start_day: JSON.stringify(props.start.getDate()),
        end_year: JSON.stringify(props.end.getFullYear()),
        end_month: JSON.stringify(props.end.getMonth()),
        end_day: JSON.stringify(props.end.getDate())
      })}).then(res => res.json())
      .then(data => {this.setState({events: data.events});},
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        error => {this.setState({error});}
      )
  }

  render() {
    return (
      <div className="App">
        <p>{this.state.error}</p>
        <p>My Token = {window.token}</p>
        <Calendar
          localizer={localizer}
          defaultDate={new Date()}
          defaultView="month"
          events={this.state.events}
          views={['month']}
          style={{ height: "100vh" }}
          onRangeChange={this.requestAvailableDates}
        />
      </div>
    );
  }
}

export default App;
