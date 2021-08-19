<template>
  <section class="bg-transparent">
    <nav
      class="navbar flex items-center border-b-2
      border-gray-200 justify-between py-8 pr-20 px-10"
    >
      <div class="left">
        <div class="relative input-width">
          <input
            placeholder="search"
            type="Search"
            class="bg-transparent w-full h-10 input-left-padding
            rounded-xl border border-gray-200"
          />
          <span class="absolute search-icon">
            <icon icon="search" class="ml-5 text-gray-400 text-sm" />
          </span>
        </div>
      </div>
      <div class="right flex items-center justify-between">
        <span>
          <img src="../../assets/images/svgs/Group 140.svg" class="w-5">
        </span>
      </div>
    </nav>
  </section>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>
