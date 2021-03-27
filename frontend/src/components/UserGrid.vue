<template>
  <v-container fluid style="height: 100vh">
    <template>
      <v-row
        v-for="(userRow, index) in userRows"
        :key="`row-${index}`"
        :style="`height: ${100 / userRows.length}%`"
      >
        <v-col v-for="(user, index) in userRow" :key="`col-${index}`">
          <User
            :name="user.name"
            :isSpeaking="user.isSpeaking"
            :emotion="user.emotion"
          />
        </v-col>
      </v-row>
    </template>
  </v-container>
</template>

<script>
import User from "./User.vue";

export default {
  name: "UserGrid",
  props: {
    users: Array,
  },
  components: {
    User,
  },
  computed: {
    numUsers() {
      return this.users.length;
    },
    userRows() {
      const users = this.users;
      const numUsersInRow = this.numColumns;
      const result = [];

      // Split users array into array of rows of users
      for (let i = 0; i < users.length; i += numUsersInRow) {
        result.push(users.slice(i, i + numUsersInRow));
      }

      console.log(users, numUsersInRow, result);

      // Truncate result to number of available rows
      return result.slice(0, this.numRows);
    },
    numColumns() {
      // Get current window's width
      const windowWidth = this.$vuetify.breakpoint.width;
      // Get each user box's width (with appropriate margins)
      const userWidth = this.getComponentDim(130, 12);

      // Get number of columns needed
      const numColumnsSparse = Math.ceil(Math.sqrt(this.numUsers) * 1.2);
      const maxNumColumns = Math.floor(windowWidth / userWidth);

      return Math.min(numColumnsSparse, maxNumColumns);
    },
    numRows() {
      // Get current window's height
      const windowHeight = this.$vuetify.breakpoint.height;
      // Get each user box's height (with appropriate margins)
      const userHeight = this.getComponentDim(130, 12);

      return Math.floor(windowHeight / userHeight);
    },
  },
  methods: {
    getComponentDim: (boxDim, padding) => boxDim + padding * 2 + 1,
  },
};
</script>
