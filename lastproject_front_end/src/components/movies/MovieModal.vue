<template>
  <div>
    <b-button v-b-modal.modal-center v-b-modal.modal-xl>Movie Page</b-button>
    <div :id="`movie-${movie.id}`">

      <b-modal id="modal-center" centered :title="movie.title">
        <div>
          <b-card :img-src="movie.poster_url" :img-alt="movie.title" img-left class="mb-3">
            <b-card-text>
              



            </b-card-text>
          </b-card>
        </div>
      </b-modal>

    </div>

  </div>
</template>

<script>
  export default {
    name: 'MovieModal',
    props: {
      movie: Object,
    }


  }
</script>

<style>

</style>