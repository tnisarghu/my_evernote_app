<template>
  <div v-if="note">
    <h2>{{ note.title }}</h2>
    <p>{{ note.content }}</p>
    <router-link :to="`/notes/${note.id}/edit`">Edit</router-link>
    <button @click="deleteNote">Delete</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      note: null,
    };
  },
  mounted() {
    this.fetchNote();
  },
  methods: {
    fetchNote() {
      const noteId = this.$route.params.id;
      axios.get(`/api/notes/${noteId}`)
        .then(response => {
          this.note = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    deleteNote() {
      const noteId = this.$route.params.id;
      axios.delete(`/api/notes/${noteId}`)
        .then(() => {
          this.$router.push('/notes');
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
