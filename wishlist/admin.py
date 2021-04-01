from django.contrib import admin
from .models import Wishlist, WishlistItem

import nested_admin


class WishlistItemAdmin(nested_admin.NestedStackedInline):
    model = WishlistItem


class WishlistAdmin(nested_admin.NestedModelAdmin):
    inline = [WishlistItemAdmin]


admin.site.register(Wishlist, WishlistAdmin)