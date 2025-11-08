<template>
    <div class="p-2 lg:p-4">
        <button @click="pickRoomCards">Room cards</button>
    </div>
</template>

<script setup>
import { useFieldStore } from '../../stores/FieldStore';



const fieldStore = useFieldStore()

function pickRoomCards(){
    fieldStore.pickRoomCards()
}
</script>