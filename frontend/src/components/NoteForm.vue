<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="form.title">
    </div>
    <div>
      <label for="content">Content:</label>
      <textarea id="content" v-model="form.content"></textarea>
    </div>
    <button type="submit">Save Note</button>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  methods: {
    submitForm() {
      const noteId = this.$route.params.id;
      const method = noteId ? 'put' : 'post';
      const url = noteId ? `/api/notes/${noteId}` : '/api/notes';
      axios[method](url, this.form)
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
