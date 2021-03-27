<template>
  <div class="user" :class="speakingBorder">
    <div class="emotion">{{ emotion }}</div>
    <div class="name">{{ name }}</div>
  </div>
</template>

<script>
export default {
  name: "User",
  props: {
    name: String,
    isSpeaking: Boolean,
    emotion: String,
  },
  computed: {
    speakingBorder() {
      return this.$props.isSpeaking ? "speaking" : "silent";
    },
  },
};
</script>

<style lang="scss" scoped>
.user {
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  min-width: 130px;
  min-height: 130px;
  height: 100%;

  .emotion {
    font-size: 4rem;
    padding-bottom: 5vh;
  }

  .name {
    font-family: "Roboto", sans-serif;
    color: #03dac5;
    font-size: 1.3rem;
    position: absolute;
    bottom: 0;
    left: 10px;
    margin: 0;
    opacity: 0.5;
  }

  * {
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    -o-user-select: none;
    user-select: none;
  }
}

.speaking {
  background-color: #332940;
}

.silent {
  background-color: #1f1b24;
}
</style>
