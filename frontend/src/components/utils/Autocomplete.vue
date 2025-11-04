<template>
  <div class="relative w-full max-w-xs">
    <div
      v-if="selectedItem"
      class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg flex justify-between items-center text-gray-900"
    >
      <span>{{ selectedItem.name }}</span>
      <button
        @click="clearSelection"
        type="button"
        class="ml-2 text-gray-400 hover:text-gray-700 focus:outline-none transition-colors"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>

    <div v-else>
      <input
        type="text"
        v-model="query"
        placeholder="Search..."
        class="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200"
      />
      <div
        v-if="filteredItems.length > 0"
        class="absolute z-10 w-full mt-1 bg-white border border-gray-200 rounded-lg shadow-xl max-h-60 overflow-y-auto"
      >
        <ul>
          <li
            v-for="item in filteredItems"
            :key="item.id"
            @mousedown.prevent="selectItem(item)"
            class="px-4 py-2 cursor-pointer hover:bg-gray-100 text-gray-800"
          >
            {{ item.name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  items: {
    type: Array,
    required: true,
  },
  onSubmit: {
    type: Function,
    required: true,
  },
  key_field: {
    type: String,
    required: true,
  },
});

const query = ref('');
const selectedItem = ref(null);

const filteredItems = computed(() => {
  if (query.value === '') {
    return [];
  }
  return props.items.filter(item =>
    item.name.toLowerCase().includes(query.value.toLowerCase())
  );
});

const selectItem = (item) => {
  selectedItem.value = item;
  props.onSubmit(item);
  query.value = '';
};

const clearSelection = () => {
  selectedItem.value = null;
  props.onSubmit(undefined); 
};
</script>