<template>
    <div v-if="$store.state.isLoading" class="text-center my-5">
      <div
        class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full border-x-gray-500 border-t-gray-500"
        role="status"
      ></div>
    </div>
</template>

<script>
    export default{
        name: "loading-bar",
        data(){
            return {}
        }
    }
</script>