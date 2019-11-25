<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <div>
      <input @click="addmovie" type="submit">나와라
      {{ movie.title}}
    </div>
    <MovieHome />
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router';
const axios = require('axios'); 
import MovieHome from '../components/MovieHome';


export default {
  name: 'home',
  data () {
    return {
      movie: [],
    }
  },
  components: {
    MovieHome,
  },
  methods: {
    addmovie() {
      axios.get('http://localhost:8000/api/movies/')
      .then(res=> {
        this.movie.push(res.data);
        router.push('/');
        console.log(res)
      })
    }
  }
}
</script>
