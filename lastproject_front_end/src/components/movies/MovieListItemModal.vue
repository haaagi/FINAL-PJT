<template>
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">

  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">

        <h5 class="modal-title">{{ movie.title }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

        <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.name">
        <div>
        </div>
        <hr>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>



  <!-- <div :id="`movie-${movie.id}`">
    <b-modal id="modal-center" centered title="BootstrapVue">
      <div class="my-4">
        <div>
          <b-card :img-src="movie.poster_url" img-left class="mb-3">
            <b-card-text>
              <h4>{{ movie.title }}</h4>
              <span>({{ movie.title_eng }})</span>

              <div>
                박스오피스 순위: {{ movie.rank }} | ({{ movie.audience }})
                관람등급: {{ movie.watch_grade }}
              </div>
              <hr>
              <div>
                {{ movie.description }}
                <a :href="movie.naver_link">...더보기</a>
              </div>
            </b-card-text>
          </b-card>
        </div>
      </div>
    </b-modal>
  </div> -->

</template>

<script>
  export default {
    name: 'MovieListItemModal',
    props: {
      movie: Object,
    }
  }
</script>

<style>

</style>