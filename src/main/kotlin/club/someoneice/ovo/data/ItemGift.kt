package club.someoneice.ovo.data

import club.someoneice.ovo.data.helper.ItemGiftHelper

data class ItemGift(
    val name: String,
    val localization_name: String,
    val texture_name: String,
    val max_size: Int,
    val items: ArrayList<ItemGiftHelper>,
    val group: String
)
