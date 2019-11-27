<template>
  <div class="movie-detail-page">
    <MovieDetail :movie="movie" />

    
    <router-view/>
    

  </div>
</template>


<script>
import MovieDetail from'../components/movies/MovieDetail';
import router from '../router';

export default {
  name: 'home',
  components: {
    MovieDetail,
  },
  data () {
    return {
      movie: Object,
    }
  },
  // emit: {
  //   movie: Object,
  // },
  mounted () {
      router.push("/moviedetailpage");
    },

}

</script>

<style>
</style>