<template>
  <div class="p-4">
    <div
      :class="[
        'drop-zone border-2 border-dashed border-gray-300 rounded-lg p-10 text-center text-gray-500 cursor-pointer transition-colors duration-300',
        { 'bg-blue-50 border-blue-500': isDragging },
      ]"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="onDrop"
      @click="openFileInput"
    >
      <p class="m-0 text-lg">Drag & Drop images here or click to upload</p>
      <input
        type="file"
        ref="fileInput"
        multiple
        accept="image/*"
        @change="onFileSelected"
        style="display: none"
      />
    </div>

    <div
      v-if="images.length > 0"
      class="slider-container relative w-full max-w-2xl mx-auto mt-5 overflow-hidden rounded-lg shadow-lg"
    >
      <div
        class="slider-track flex transition-transform duration-500 ease-in-out"
        :style="{ transform: sliderTransform }"
      >
        <div
          v-for="image in images"
          :key="image.id"
          class="slide min-w-full box-border"
        >
          <div
            class="h-96 w-full flex items-center justify-center bg-gray-100"
          >
            <img
              :src="image.url"
              :alt="image.title"
              class="max-w-full max-h-full object-contain w-full"
            />
          </div>
          <div class="p-3 flex items-center gap-3 bg-white border-t">
            <input
              type="text"
              v-model="image.title"
              class="flex-1 w-full p-2 border border-gray-300 rounded focus:ring-blue-500 focus:border-blue-500"
              placeholder="Image name"
            />
            <button
              @click="removeImage(image.id)"
              class="bg-white flex-shrink-0 p-2 text-red-500 rounded-full hover:bg-red-100 hover:text-red-700 transition-colors"
              aria-label="Delete image"
            >
              <TrashIcon/>
            </button>
          </div>
        </div>
      </div>
      <button
        @click="prev"
        class="slider-nav prev absolute top-1/2 -translate-y-1/2 bg-black bg-opacity-50 text-white border-none rounded-full w-10 h-10 text-2xl cursor-pointer z-10 flex items-center justify-center transition-colors duration-300 hover:bg-opacity-80 left-2.5"
        v-if="currentIndex > 0"
      >
        &#10094;
      </button>
      <button
        @click="next"
        class="slider-nav next absolute top-1/2 -translate-y-1/2 bg-black bg-opacity-50 text-white border-none rounded-full w-10 h-10 text-2xl cursor-pointer z-10 flex items-center justify-center transition-colors duration-300 hover:bg-opacity-80 right-2.5"
        v-if="currentIndex < images.length - 1"
      >
        &#10095;
      </button>
    </div>
    <ClearInput/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useFieldStore } from '@/stores/FieldStore.js'
import { useModalStore } from '@/stores/ModalStore.js'
import ClearInput from './ClearInput.vue'
import TrashIcon from '@/components/icons/TrashIcon.vue'
import ImageDeleteModal from '../modals/ImageDeleteModal.vue'

const fieldStore = useFieldStore()
const modalStore = useModalStore()
const images = computed(() => fieldStore.getCards)
const fileInput = ref(null)
const isDragging = ref(false)
const currentIndex = ref(0)

const getBaseName = (fileName) => {
  return fileName.lastIndexOf('.') > 0
    ? fileName.substring(0, fileName.lastIndexOf('.'))
    : fileName
}

const processFiles = (files) => {
  fieldStore.removeAllCards()
  fieldStore.setRawFiles(files)
  for (const file of files) {
    if (file.type.startsWith('image/')) {
      const id = crypto.randomUUID()
      const url = URL.createObjectURL(file)
      const title = getBaseName(file.name)

      const newImage = { id, url, title, isActive: true }
      fieldStore.addCard(newImage)
    }
  }
}


const removeImage = (id) => {
  function deleteImage(){
      const index = images.value.findIndex((img) => img.id === id)
      if (index === -1) return

      URL.revokeObjectURL(images.value[index].url)
      images.value.splice(index, 1)
      fieldStore.deleteCard(id)

      if (currentIndex.value >= images.value.length && images.value.length > 0) {
        currentIndex.value = images.value.length - 1
      } else if (images.value.length === 0) {
        currentIndex.value = 0
      }
  }
  modalStore.openModal(ImageDeleteModal, { callbackFun: deleteImage })
}

const onDrop = (event) => {
  isDragging.value = false
  processFiles(event.dataTransfer.files)
}

const onFileSelected = (event) => {
  processFiles(event.target.files)
}

const openFileInput = () => {
  fileInput.value.click()
}

const sliderTransform = computed(() => {
  return `translateX(-${currentIndex.value * 100}%)`
})

const next = () => {
  if (currentIndex.value < images.value.length - 1) {
    currentIndex.value++
  }
}

const prev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}
</script>

<style scoped></style>