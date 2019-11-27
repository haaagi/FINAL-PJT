<template>
  <div :id="`movie-${movie.id}`">
    <div>
  <b-card no-body class="overflow-hidden" style="max-width: 540px;">
    <b-row no-gutters>
      <b-col md="6">
        <b-card-img :src="movie.poster_url" :alt="movie.title" class="rounded-0"></b-card-img>
      </b-col>
      <b-col md="6">
        <b-card-body :title="movie.title">
          <b-card-text>
            This is a wider card with supporting text as a natural lead-in to additional content.
            This content is a little bit longer.
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</div>
  </div>
</template>

<script>
  export default {
    name: 'MovieDetail',
    props: {
      movie: Object,
    }


  }
</script>

<style>

</style>