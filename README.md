# djjoecalendar
Availability Calendar for DJJoe Website

### Frontend:
The frontend of this system is a React-js site generated using
[`react-big-calendar`](https://github.com/jquense/react-big-calendar)
whose documentation may be found [here](https://jquense.github.io/react-big-calendar/examples/index.html#api).

### Backend:
The backend is a Python/FastAPI server responsible for serving the static files
and accessing the sensitive information (private calendars) to make appropriate
queries relating to available dates.

### Linking frontend and backend (React/FastAPI):
With some minor modifications made to the FastAPI configuration,
[this guide on using Flask and React](https://blog.learningdollars.com/2019/11/29/how-to-serve-a-reactapp-with-a-flask-server/)
was used to develop the link between the two ecosystems.

## Rebuilding React Components for Serving

From the `frontend` directory, issue the following command:

```shell
npm run build
```

## Running Server for Development

From the `backend` directory, issue the following command:

```shell
uvicorn main:app --reload
```