<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <MovieHome />
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router';
import MovieHome from '../components/MovieHome';


export default {
  name: 'home',
  components: {
    MovieHome,
  }
}
</script>
