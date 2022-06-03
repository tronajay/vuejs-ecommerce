<template>
  <div
    v-if="$store.state.isLoading"
    class="absolute top-0 left-0 right-0 bottom-0 w-full z-50 overflow-hidden bg-gray-700 opacity-30 rounded-lg flex flex-col items-center justify-center"
  >
  <div
        class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full border-x-gray-500 border-t-gray-500"
        role="status"
      ></div>
  </div>
</template>

<script>
export default{
    name: "loading-bar-contain",
}

</script>
