<template>
  <div>
    <h1>Your Notes</h1>
    <ul>
      <li v-for="note in notes" :key="note.id">
        <router-link :to="`/notes/${note.id}`">{{ note.title }}</router-link>
      </li>
    </ul>
    <router-link to="/notes/create">Create New Note</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      notes: [],
    };
  },
  mounted() {
    this.fetchNotes();
  },
  methods: {
    fetchNotes() {
      axios.get('/api/notes')
        .then(response => {
          this.notes = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
