<script lang="ts">
  import type { TableEntry } from '@mathesar/api/types/tables';
  import { tables as tablesDataStore } from '@mathesar/stores/tables';
  import type { SelectProps } from '@mathesar-component-library/types';
  import SelectTable from './SelectTable.svelte';

  export let value: TableEntry | undefined = undefined;
  export let prependBlank = false;
  export let autoSelect: SelectProps<TableEntry | undefined>['autoSelect'] =
    'first';

  $: tables = [...$tablesDataStore.data.values()];
</script>

<SelectTable {tables} bind:value {prependBlank} {autoSelect} on:change />
