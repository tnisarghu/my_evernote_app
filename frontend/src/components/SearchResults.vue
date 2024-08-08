<template>
  <div v-if="searchResults.length > 0">
    <h2>Search Results for "{{ searchQuery }}"</h2>
    <ul>
      <li v-for="result in searchResults" :key="result.objectID">
        <router-link :to="`/notes/${result.objectID}`">{{ result.title }}</router-link>
      </li>
    </ul>
  </div>
  <div v-else>
    No results found for "{{ searchQuery }}".
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['searchQuery'],
  data() {
    return {
      searchResults: [],
    };
  },
  mounted() {
    this.fetchSearchResults();
  },
  methods: {
    fetchSearchResults() {
      axios.get(`/api/search?q=${this.searchQuery}`)
        .then(response => {
          this.searchResults = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
