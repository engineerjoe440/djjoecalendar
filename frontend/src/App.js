import React, { Component } from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import toast, { Toaster, CheckmarkIcon } from 'react-hot-toast';
import moment from "moment";

import "./App.css";
import "react-big-calendar/lib/css/react-big-calendar.css";

// Function to help secure usage of `_blank`
const openInNewTab = (url) => {
  const newWindow = window.open(url, '_blank', 'noopener,noreferrer')
  if (newWindow) newWindow.opener = null
}

// Localizer
const localizer = momentLocalizer(moment);

const subjectDate = (eventDate) => {
  return encodeURIComponent(eventDate.split("T")[0] + " Event Quote Request")
}

// Available Date Callback
const availDate = (eventInfo) => toast((t) => (
    <span>
      That date is available! {'  '}
      <button onClick={() => openInNewTab(
        'https://www.djjoeidaho.com/contact-us?subject=' + subjectDate(eventInfo.start)
      )}>Snag It!</button>
    </span>
  ),
  {
    icon: <CheckmarkIcon />,
    duration: 10000,
  }
);

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      error: null,
      events: []
    };

    // Bind Class Method
    this.requestAvailableDates = this.requestAvailableDates.bind(this);
  }

  requestAvailableDates(props) {
    // Make POST Request with JSON Payload
    fetch("/api/getavailability", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        start: props.start,
        end: props.end
      })}).then(res => res.json())
      .then(data => {this.setState({events: data.events});},
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        error => {
          this.setState({error});
          toast.error("ERROR: "+JSON.stringify(error));
        }
      )
  }

  render() {
    return (
      <div className="App">
        <Toaster position="bottom-right"/>
        <Calendar
          localizer={localizer}
          defaultDate={new Date()}
          defaultView="month"
          events={this.state.events}
          views={['month']}
          style={{ height: "100vh" }}
          onRangeChange={this.requestAvailableDates}
          onSelectEvent={availDate}
        />
      </div>
    );
  }
}

export default App;
