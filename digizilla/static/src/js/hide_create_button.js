/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";

patch(ListController.prototype, {
    renderButtons() {
        super.renderButtons();
        if (this.$buttons) {
            this.$buttons.find('.o_list_button_add').hide();
        }
    },
});
