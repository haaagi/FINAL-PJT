<template>
  <div class="movie-detail-page">
    <MovieDetailPage :movie="movie"/>
  </div>
</template>


<script>
import MovieDetail from'../components/movies/MovieDetail';

export default {
  name: 'home',
  components: {
    // MovieDetail,
  },
  data () {
    return {
      movie: Object,
    }
  },

}

</script>

<style>
</style>