<template>
  <v-container fluid>
    <v-row>
      <template v-for="(user, index) in truncatedUsers">
        <v-col :key="index">
          <User :userData="user" />
        </v-col>
        <v-responsive
          v-if="doSplit(index)"
          :key="`width-${index}`"
          width="100%"
        />
      </template>
    </v-row>
  </v-container>
</template>

<script>
import User from "./User.vue";

let maxUsers = 20;

export default {
  name: "UserGrid",
  props: {
    users: Array,
  },
  components: {
    User,
  },
  computed: {
    numColumns() {
      const windowWidth = this.$vuetify.breakpoint.width;
      const userBoxWidth = 130;
      const sidePadding = 12;
      const userWidth = userBoxWidth + sidePadding * 2 + 1;

      const numUsers = this.users.length;
      const numColumns = Math.ceil(Math.sqrt(numUsers));

      const doManualSplit = numColumns * userWidth < windowWidth;
      const columns = doManualSplit ? numColumns : -1;

      return { doManualSplit, columns };
    },
    truncatedUsers() {
      return this.users.slice(0, maxUsers);
    },
  },
  methods: {
    doSplit(index) {
      const { doManualSplit, columns } = this.numColumns;

      if (doManualSplit) {
        return index % columns === columns - 1;
      } else {
        return false;
      }
    },
  },
};
</script>
