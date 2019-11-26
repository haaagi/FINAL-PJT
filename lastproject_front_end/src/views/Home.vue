<template>
  <div class="home">
    <MovieList :movies="movies" />
  </div>
</template>

<script>

// import router from '../router';
const axios = require('axios'); 
// import MovieHome from '../components/MovieHome';
import MovieList from'../components/movies/MovieList';

export default {
  name: 'home',
  components: {
    MovieList,
  },
  data () {
    return {
      movies: [],
    }
  },
  created () {
    axios.get('http://localhost:8000/api/movies/')
      .then(res=> this.movies = res.data)
      .catch(err => console.error(err))
  }
}


</script>

